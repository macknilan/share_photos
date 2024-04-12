#
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from apps.users.models import Profile, User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    """
    FUNCIÓN PARA CREAR EL PERFIL DEL USUARIO AL CREAR UN USUARIO
    """
    user = instance
    if created:
        Profile.objects.create(
            user=user,
            email=user.email
        )
    else:
        # CUANDO SE ACTUALICE EL EMAIL DEL USUARIO, SE ACTUALIZA EL EMAIL DEL PERFIL
        # PERO CREA UN LOOP, CON LA FUNCIÓN DE ABAJO, SE SOLUCIONA `if user.email != profile.email:`
        profile = get_object_or_404(Profile, user=user)
        profile.email = user.email


@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    """
    FUNCIÓN PARA CUANDO SE ACTUALICE EL EMAIL EN EL PERFIL, SE ACTUALICE EL EMAIL DEL USUARIO
    """
    profile = instance
    if not created:  # CUANDO ES FALSE, ES POR QUE SE ESTÁ ACTUALIZANDO `created == False`
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()





