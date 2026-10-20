from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import (
    EvaluacionEmocional,
    UbicacionPaciente
)


def crear_evaluacion(request):
    if request.method == "POST":
        usuario_val = request.POST.get("usuario")
        profesional_val = request.POST.get("profesional")

        # Búsqueda segura por ID o por Username para el usuario
        usuario_obj = None
        if usuario_val:
            if str(usuario_val).isdigit():
                usuario_obj = User.objects.filter(id=int(usuario_val)).first()
            else:
                usuario_obj = User.objects.filter(username=usuario_val).first()

        # Búsqueda segura por ID o por Username para el profesional
        profesional_obj = None
        if profesional_val:
            if str(profesional_val).isdigit():
                profesional_obj = User.objects.filter(id=int(profesional_val)).first()
            else:
                profesional_obj = User.objects.filter(username=profesional_val).first()

        EvaluacionEmocional.objects.create(
            usuario=usuario_obj,
            profesional=profesional_obj,
            estado_afectivo=request.POST.get("estado_afectivo"),
            nivel_riesgo=request.POST.get("nivel_riesgo"),
            necesidades_detectadas=request.POST.get("necesidades_detectadas"),
            observaciones=request.POST.get("observaciones"),
            recomendaciones=request.POST.get("recomendaciones")
        )

        return redirect("listar_evaluaciones")

    usuarios = User.objects.all()
    return render(
        request,
        "Alejandro_07/evaluacion_emocional.html",
        {"usuarios": usuarios}
    )


def listar_evaluaciones(request):
    evaluaciones = EvaluacionEmocional.objects.all()

    return render(
        request,
        "Alejandro_07/listar_evaluaciones.html",
        {
            "evaluaciones": evaluaciones
        }
    )


def registrar_ubicacion(request):
    if request.method == "POST":
        paciente_val = request.POST.get("paciente")
        autorizacion = request.POST.get("autorizacion")

        # Búsqueda segura por ID o por Username para el paciente
        paciente_obj = None
        if paciente_val:
            if str(paciente_val).isdigit():
                paciente_obj = User.objects.filter(id=int(paciente_val)).first()
            else:
                paciente_obj = User.objects.filter(username=paciente_val).first()

        if paciente_obj:
            # CAMBIADO: Usamos .create() para agregar una nueva entrada
            # en lugar de sobrescribir la existente con update_or_create()
            UbicacionPaciente.objects.create(
                paciente=paciente_obj,
                latitud=request.POST.get("latitud"),
                longitud=request.POST.get("longitud"),
                autorizacion=True if autorizacion else False,
                motivo=request.POST.get("motivo")
            )

        return redirect("listar_ubicaciones")

    usuarios = User.objects.all()
    return render(
        request,
        "Alejandro_07/ubicacion_paciente.html",
        {"usuarios": usuarios}
    )


def listar_ubicaciones(request):
    ubicaciones = UbicacionPaciente.objects.all()

    return render(
        request,
        "Alejandro_07/listar_ubicaciones.html",
        {
            "ubicaciones": ubicaciones
        }
    )