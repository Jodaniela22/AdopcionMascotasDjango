from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Persona, Mascota, Adopcion


def index(request):
    return render(request, 'index.html')

# Crear nueva persona
def nueva_persona(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula_per', '').strip()
        nombres = request.POST.get('nombres_per', '').strip()
        apellidos = request.POST.get('apellidos_per', '').strip()
        correo = request.POST.get('correo_per', '').strip()
        telefono = request.POST.get('telefono_per', '').strip()
        direccion = request.POST.get('direccion_per', '').strip()

        if cedula and nombres and apellidos and correo:
            try:
                Persona.objects.create(
                    cedula_per=cedula,
                    nombres_per=nombres,
                    apellidos_per=apellidos,
                    correo_per=correo,
                    telefono_per=telefono,
                    direccion_per=direccion
                )
                messages.success(request, "Persona registrada correctamente.")
                return redirect('listar_persona')
            except Exception as e:
                messages.error(request, f"Error al registrar la persona: {str(e)}")
        else:
            messages.error(request, "Los campos cédula, nombres, apellidos y correo son obligatorios.")

    return render(request, 'persona/nueva_persona.html')


# Listar personas
def listar_persona(request):
    personas = Persona.objects.all()
    return render(request, 'persona/listar_persona.html', {'personas': personas})


# Editar persona
def editar_persona(request, id_per):
    persona = get_object_or_404(Persona, pk=id_per)

    if request.method == 'POST':
        cedula = request.POST.get('cedula_per', '').strip()
        nombres = request.POST.get('nombres_per', '').strip()
        apellidos = request.POST.get('apellidos_per', '').strip()
        correo = request.POST.get('correo_per', '').strip()
        telefono = request.POST.get('telefono_per', '').strip()
        direccion = request.POST.get('direccion_per', '').strip()

        if not cedula or not nombres or not apellidos or not correo:
            messages.error(request, "Los campos cédula, nombres, apellidos y correo son obligatorios.")
        else:
            try:
                persona.cedula_per = cedula
                persona.nombres_per = nombres
                persona.apellidos_per = apellidos
                persona.correo_per = correo
                persona.telefono_per = telefono
                persona.direccion_per = direccion
                persona.save()
                messages.success(request, "Persona actualizada correctamente.")
                return redirect('listar_persona')
            except Exception as e:
                messages.error(request, f"Error al actualizar la persona: {str(e)}")

    return render(request, 'persona/editar_persona.html', {'persona': persona})


# Eliminar persona
def eliminar_persona(request, id_per):
    persona = get_object_or_404(Persona, pk=id_per)
    try:
        persona.delete()
        messages.success(request, "Persona eliminada correctamente.")
    except Exception as e:
        messages.error(request, f"Error al eliminar la persona: {str(e)}")

    return redirect('listar_persona')

def nueva_mascota(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        especie = request.POST.get('especie')
        raza = request.POST.get('raza')
        sexo = request.POST.get('sexo')
        edad = request.POST.get('edad')
        estado = request.POST.get('estado')
        observaciones = request.POST.get('observaciones')

        if nombre and especie:
            try:
                Mascota.objects.create(
                    nombre_mas=nombre,
                    especie_mas=especie,
                    raza_mas=raza,
                    sexo_mas=sexo,
                    edad_anios_mas=edad or 0,
                    estado_mas=estado or 'Disponible',
                    observaciones_mas=observaciones
                )
                messages.success(request, "Mascota registrada correctamente.")
                return redirect('listar_mascota')
            except Exception as e:
                messages.error(request, f"Error al registrar la mascota: {str(e)}")
        else:
            messages.error(request, "Nombre y especie son obligatorios.")

    return render(request, 'mascota/nueva_mascota.html')

# Listar
def listar_mascota(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascota/listar_mascota.html', {'mascotas': mascotas})

# Editar
def editar_mascota(request, id):
    mascota = get_object_or_404(Mascota, pk=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre').strip()
        especie = request.POST.get('especie').strip()
        raza = request.POST.get('raza').strip()
        sexo = request.POST.get('sexo').strip()
        edad = request.POST.get('edad').strip()
        estado = request.POST.get('estado').strip()
        observaciones = request.POST.get('observaciones').strip()

        if not nombre or not especie:
            messages.error(request, "Nombre y especie son obligatorios.")
        else:
            try:
                mascota.nombre_mas = nombre
                mascota.especie_mas = especie
                mascota.raza_mas = raza
                mascota.sexo_mas = sexo
                mascota.edad_anios_mas = edad or 0
                mascota.estado_mas = estado or 'Disponible'
                mascota.observaciones_mas = observaciones
                mascota.save()
                messages.success(request, "Mascota actualizada correctamente.")
                return redirect('listar_mascota')
            except Exception as e:
                messages.error(request, f"Error al actualizar la mascota: {str(e)}")

    return render(request, 'mascota/editar_mascota.html', {'mascota': mascota})

# Eliminar
def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, pk=id)
    try:
        mascota.delete()
        messages.success(request, "Mascota eliminada correctamente.")
    except Exception as e:
        messages.error(request, f"Error al eliminar la mascota: {str(e)}")
    return redirect('listar_mascota')



def nueva_adopcion(request):
    personas = Persona.objects.all()
    mascotas = Mascota.objects.filter(estado_mas='Disponible')
    
    if request.method == 'POST':
        persona_id = request.POST.get('persona')
        mascota_id = request.POST.get('mascota')
        estado = request.POST.get('estado') or 'Solicitada'
        documento = request.POST.get('documento', '')

        if persona_id and mascota_id:
            try:
                persona = get_object_or_404(Persona, pk=persona_id)
                mascota = get_object_or_404(Mascota, pk=mascota_id)
                adopcion = Adopcion.objects.create(
                    persona=persona,
                    mascota=mascota,
                    estado_ado=estado,
                    documento_ado=documento
                )
                # Cambiar estado de la mascota a "En Adopción" para que no aparezca en otras solicitudes
                mascota.estado_mas = 'En Adopción'
                mascota.save()
                messages.success(request, "Adopción registrada correctamente.")
                return redirect('listar_adopcion')
            except Exception as e:
                messages.error(request, f"Error al registrar la adopción: {str(e)}")
        else:
            messages.error(request, "Debe seleccionar una persona y una mascota.")

    return render(request, 'adopcion/nueva_adopcion.html', {'personas': personas, 'mascotas': mascotas})

# Listar
def listar_adopcion(request):
    adopciones = Adopcion.objects.select_related('persona', 'mascota').all()
    return render(request, 'adopcion/listar_adopcion.html', {'adopciones': adopciones})

# Editar
def editar_adopcion(request, id):
    adopcion = get_object_or_404(Adopcion, pk=id)
    personas = Persona.objects.all()
    mascotas = Mascota.objects.all()

    if request.method == 'POST':
        persona_id = request.POST.get('persona')
        mascota_id = request.POST.get('mascota')
        estado = request.POST.get('estado')
        documento = request.POST.get('documento', '')

        if not persona_id or not mascota_id:
            messages.error(request, "Debe seleccionar una persona y una mascota.")
        else:
            try:
                adopcion.persona = get_object_or_404(Persona, pk=persona_id)
                adopcion.mascota = get_object_or_404(Mascota, pk=mascota_id)
                adopcion.estado_ado = estado
                adopcion.documento_ado = documento
                adopcion.save()
                messages.success(request, "Adopción actualizada correctamente.")
                return redirect('listar_adopcion')
            except Exception as e:
                messages.error(request, f"Error al actualizar la adopción: {str(e)}")

    return render(request, 'adopcion/editar_adopcion.html', {'adopcion': adopcion, 'personas': personas, 'mascotas': mascotas})

# Eliminar
def eliminar_adopcion(request, id):
    adopcion = get_object_or_404(Adopcion, pk=id)
    try:
        # Cambiar estado de la mascota si se elimina la adopción
        mascota = adopcion.mascota
        mascota.estado_mas = 'Disponible'
        mascota.save()
        adopcion.delete()
        messages.success(request, "Adopción eliminada correctamente.")
    except Exception as e:
        messages.error(request, f"Error al eliminar la adopción: {str(e)}")
    return redirect('listar_adopcion')