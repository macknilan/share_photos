# FORMS FOR USER ALLAUTH SIGNUP, LOGIN, AND PASSWORD RESET.


from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm
from django import forms


class MyCustomLoginForm(LoginForm):
    """
    STYLE CUSTOMIZATION FOR THE LOGIN FORM -django-alluth-
    """
    remember = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"type": "checkbox", "class": "w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"}))

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)

        self.fields["login"].widget = forms.TextInput(attrs={
            "id": "id_login",
            "type": "text",
            "placeholder": "name@mail.com",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        })
        self.fields["password"].widget = forms.PasswordInput(attrs={
            "id": "id_password",
            "type": "password",
            "placeholder": "••••••••",
            "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        })
        self.fields["remember"].widget = forms.CheckboxInput(attrs={
            "type": "checkbox",
            "class": "w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"
        })
        #
        self.fields['login'].label = "Email"
        self.fields['password'].label = "Password"
        self.fields['remember'].label = "Remember"

    def login(self, *args, **kwargs):

        # You must return the original result.
        # Add your custom login logic here
        return super(MyCustomLoginForm, self).login(*args, **kwargs)


class MyCustomSignupForm(SignupForm):
    """
    STYLE CUSTOMIZATION FOR THE SIGNUP FORM -django-alluth-

    TODO: Revisar por que -password2- y -password2- no funcionan los estilos. Se modifico por medio de CSS -my_css-
    """
    email = forms.EmailField(label="Email:", max_length=255, widget=forms.EmailInput(attrs={
        "id": "id_email",
        "type": "email",
        "placeholder": "Email address",
        "autocomplete": "False",
        "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    }))
    username = forms.CharField(label="Username:", max_length=150, widget=forms.TextInput(attrs={
        "id": "id_username",
        "type": "text",
        "placeholder": "Username",
        "autocomplete": "new-password",
        "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    }))

    # password1 = forms.CharField(label="Password:", max_length=128, label_suffix="Password", widget=forms.TextInput(attrs={
    #     "id": "id_password1",
    #     "type": "password",
    #     "placeholder": "Password",
    #     "autocomplete": "new-password",
    #     "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    # }))
    # password2 = forms.CharField(label="Password (again):", max_length=128, widget=forms.TextInput(attrs={
    #     "id": "id_password2",
    #     "type": "password",
    #     "placeholder": "Password (again)",
    #     "autocomplete": "False",
    #     "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    # }))

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        # Add your own processing here.
        # You must return the original result.
        return user


class MyCustomResetPasswordForm(ResetPasswordForm):
    """
    TODO
    """
    email = forms.EmailField(label="Email:", max_length=255, widget=forms.EmailInput(attrs={
        "id": "id_email",
        "type": "email",
        "placeholder": "Email address",
        "autocomplete": "False",
        "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    }))

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a string containing the email address supplied
        email_address = super(MyCustomResetPasswordForm, self).save(request)
        # Add your own processing here.
        # Ensure you return the original result
        return email_address


