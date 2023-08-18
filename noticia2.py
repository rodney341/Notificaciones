import requests
import json

# Tu clave del servidor de FCM
fcm_server_key = "AAAATNI-_JQ:APA91bEmaNhhxzo5FGSiyar-kVF_OAQNNG8BZIkVJnCYJdD8sJu3HjtZpISxi4N3MYlcrRP4wAXiD0JJe33BvsOsmolGCR9p2Am8S3YJ5WbvwzQ1bO9J0RM4zQGDi4e2hjA76mbouZiV"

# Endpoint de la API de FCM
fcm_url = "https://fcm.googleapis.com/fcm/send"

# Encabezados de la solicitud
headers = {
    "Authorization": f"key={fcm_server_key}",
    "Content-Type": "application/json"
}

# Datos de la notificación
notification_data = {
    "to": "ezlbESgczIRfb8QpUyZtlg:APA91bEaejeNVR7UxnfEcs3L3sGsOY3ivKkVA-KuW5UDGeRqW3eT4_NHjk7iSJFXACHPldrykrVO7kmWUdaAzQ3IfiPtoc_I_BnKYvmturXV1xgq3Ex-uld4MO2ZueRrvTA6s9sBrad9",
    "notification": {
        "title": "Título de la notificación",
        "body": "Cuerpo de la notificación",
        "icon": "nombre_del_recurso_icono",
        "click_action": "ACTION_DEL_CLICK"
    }
}

# Convertir los datos a formato JSON
notification_payload = json.dumps(notification_data)

# Realizar la solicitud POST a FCM
response = requests.post(fcm_url, data=notification_payload, headers=headers)

# Imprimir la respuesta
print(response.status_code)
print(response.content)
