# 25
from requests import Session
from zeep import Client, Transport
from orders.models import Order
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import requests
import json
from django.views.decorators.csrf import csrf_exempt




class PaymentGatewayAdapter(object):
    def __init__(self):
        pass

    def create_client(self, web_service) -> Client:
        session = Session()
        session.headers = {}
        transport = Transport(session=session)
        transport.session.headers = {}  # DON'T REMOVE THIS LINE.YOU BLOCK FROM SAMAN BANK IF REMOVE THIS LINE
        return Client(web_service, transport=transport)

    def sep_request_token(self, amount,res_num, additional_data: ['', '']):
        client = self.create_client('https://sep.shaparak.ir/payments/initpayment.asmx?wsdl')
        #res_num = self.sep_generate_reservation_number()
        response = client.service.RequestToken(
            '124475329',
            res_num,
            amount,
            '0', '0', '0', '0', '0', '0',
            additional_data[0],
            additional_data[1],
            '0',
            'http://dobicho.com/payment/verify/'
        )
        token = str(response)
        return token, res_num

    def sep_verify_transaction(self, ref_num):
        client = self.create_client('https://sep.shaparak.ir/payments/referencepayment.asmx?wsdl')
        result = client.service.verifyTransaction(
            ref_num,
            '1244038829'
        )
        return result

    def sep_reverse_transaction(self, ref_num):
        client = self.create_client('https://sep.shaparak.ir/payments/referencepayment.asmx?wsdl')
        result = client.service.reverseTransaction(
            ref_num,
            "saman mid",
            "saman mid",
            "saman password"
        )
        return result

    def sep_generate_reservation_number(self):
        return StringUtils.id_generator(size=15)

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()
    test = int(total_cost)
    if request.method == 'POST':
        res_num=str(order.id)
        total =str(test)

        R =PaymentGatewayAdapter()
        tokenrequest=R.sep_request_token(amount=total,res_num=res_num, additional_data=[order.phone, order.first_name])

        token = tokenrequest
        return HttpResponse(token[0])
        return render(request, 'payment/send.html', {'token':token[0]})
    else:
        # generate token

        return render(request,
                      'payment/process.html',
                      {'order': order})

@csrf_exempt
def payment_verify(request):
    if request.method == 'POST':
        R =PaymentGatewayAdapter()

        token = request.POST.get('Token')
        ref_num = request.POST.get('RefNum')
        res_num = request.POST.get('ResNum')
        res = int(res_num)
        result = request.POST.get('State')
        order = get_object_or_404(Order, id= res)
        # create and submit transaction
        if result== 'OK':
            paied = R.sep_verify_transaction(ref_num)
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            #order.braintree_id = sendtoken.CID
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token

        return render(request,
                      'payment/process.html',
                      {'order': order})
@login_required
def payment_done(request):
    return render(request, 'payment/done.html')
@login_required
def payment_canceled(request):
    return render(request, 'payment/canceled.html')