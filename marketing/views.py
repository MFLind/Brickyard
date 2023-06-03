""" Views for Marketing """
import logging
import hashlib
from django.http import JsonResponse
from django.shortcuts import render, redirect
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from Brickyard import settings
from marketing.forms import EmailForm


logger = logging.getLogger(__name__)

mailchimp = Client()
mailchimp.set_config(
    {
        "api_key": settings.MAILCHIMP_API_KEY,
        "server": settings.MAILCHIMP_REGION,
    }
)


def mailchimp_ping_view(
      request  # pylint: disable=unused-argument
):
    """ handling testing mailchimp with ping message """
    response = mailchimp.ping.get()
    return JsonResponse(response)


def subscribe_view(request):
    """ handle subscribing view """
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data["email"]
                member_info = {
                    "email_address": form_email,
                    "status": "subscribed",
                }
                response = mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                logger.info("API call successful: {}", response)
                return redirect("subscribe-success")

            except ApiClientError as error:
                logger.error("An exception occurred: {}", error.text)
                return redirect("subscribe-fail")

    return render(
        request,
        "marketing/subscribe.html",
        {
            "form": EmailForm(),
        },
    )


def subscribe_success_view(request):
    """ handle subscribe success """
    return render(
        request,
        "marketing/message.html",
        {
            "title": "Successfully subscribed",
            "message": "You have been successfully subscribed \
            to our mailing list.",
        },
    )


def subscribe_fail_view(request):
    """ handle subscribe fail """
    return render(
        request,
        "marketing/message.html",
        {
            "title": "Failed to subscribe",
            "message": "Oops, something went wrong.",
        },
    )


def unsubscribe_view(request):
    """ handle unsubscribing view """
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data["email"]
                form_email_hash = hashlib.md5(
                    form_email.encode("utf-8").lower()
                ).hexdigest()
                member_update = {
                    "status": "unsubscribed",
                }
                response = mailchimp.lists.update_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    form_email_hash,
                    member_update,
                )
                logger.info("API call successful: {}", response)
                return redirect("unsubscribe-success")

            except ApiClientError as error:
                logger.error("An exception occurred: {}", error.text)
                return redirect("unsubscribe-fail")

    return render(
        request,
        "marketing/unsubscribe.html",
        {
            "form": EmailForm(),
        },
    )


def unsubscribe_success_view(request):
    """ handle subscribe success """
    return render(
        request,
        "marketing/message.html",
        {
            "title": "Successfully unsubscribed",
            "message": "You have been successfully unsubscribed \
            from our mailing list.",
        },
    )


def unsubscribe_fail_view(request):
    """ handle subscribe fail """
    return render(
        request,
        "marketing/message.html",
        {
            "title": "Failed to unsubscribe",
            "message": "Oops, something went wrong.",
        },
    )
