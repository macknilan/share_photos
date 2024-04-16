# FORMS FOR USER ALLAUTH SIGNUP, LOGIN, AND PASSWORD RESET.


from allauth.account.forms import LoginForm
from django import forms


class MyCustomLoginForm(LoginForm):
    """
    STYLE CUSTOMIZATION FOR THE LOGIN FORM -django-alluth-
    """
    remember = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"type": "checkbox", "class": "w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"}))

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)

        self.fields["login"].widget = forms.TextInput(attrs={"id": "id_login", "type": "text", "placeholder": "name@mail.com", "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        self.fields["password"].widget = forms.PasswordInput(attrs={"id": "id_password", "type": "password", "placeholder": "••••••••", "class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"})
        self.fields["remember"].widget = forms.CheckboxInput(attrs={"type": "checkbox", "class": "w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800"})
        #
        self.fields['login'].label = "Email"
        self.fields['password'].label = "Password"
        self.fields['remember'].label = "Remember"

    def login(self, *args, **kwargs):

        # You must return the original result.
        # Add your custom login logic here
        return super(MyCustomLoginForm, self).login(*args, **kwargs)








