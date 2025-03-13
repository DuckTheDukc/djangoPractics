from django import forms

class OtpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={

                "placeholder":"Электронная почта"

            }
        )
    )
    otp= forms.CharField(
        max_length=6,
        widget=forms.TextInput(
            attrs={
                'placeholder':"Пин-код"
            }
        )
    )




class SendOTPView(View):
    user = get_user_model()

    def post(self, request, *args, **kwargs):
        user_email=request.POST["email"]
        try:
            if not self.user.objects.exclude(email = user_email).exists():
                self.user.objects.create_user(email=user_email)

            if OTPService.get_stored_otp(user_email)
            OTPService.send_otp_email(user_email,otp_code)

            return HttpResponse("Вам на почту пришел пин-код", status=201)
        except UnreadablePostError:
            return HttpResponse("Некорректные данные запроса", status=400)
        

class Authentication(MixinFormValidTemplate, FormView):
    model=get_user_model()
    form_class=OtpForm
    template_name='otp_auth.html'
    success_template='blank_page.html'
    context_object_name="website"
    succes_url="/"

    def post(self,request,*args,**kwargs):
        form=self.form_class(self.request.Post)
        if form.is_Valid():
            if OTPService.verify_otp(form.cleaned_data['email'],form.cleaned_data['otp']):
                user=authenticate(
                    self.request,
                    username=form.cleaned_data['email'],
                    otp=form.cleaned_data['otp']
                )

                if user is not None:
                    login(self.request, user)
                    OTPService.delete_otp(form.cleaned_data['email'])
                    return self.form_valid(form)
                return self.form_invalid(form)
            else:
                form.errors["otp"] = "Пин-код не верный"
            return self.form_invalid(form)