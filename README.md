# HOTEL RESERVATION APP

Una API construida en Django REST Framework que permite ver, crear, actualizar y eliminar reservas de hotel

Las rutas para la aplicación están en reservas.urls y se puede acceder por **"hotel-app/reservations/"**

![Screenshot](img/urls.png)

**Depende de el método que mandes recibirás una respuesta**

## API Reference

### Get all reservations > Muestra todas las reservaciones

```http
  GET /hotel-app/reservations/
```
![Screenshot](img/GET_all.png)

### Get a reservation > Muestra una reservación

```http
  GET /hotel-app/reservations/${id}
```
![Screenshot](img/GET_one.png)

### POST reservation > Crea una nueva reservación

```http
  POST /hotel-app/reservations/
```
![Screenshot](img/POST_one.png)

### PUT reservation > Actualiza una reservación existente

```http
  PUT /hotel-app/reservations/
```
![Screenshot](img/UPDATE_one.png)

### DELETE reservation > Elimina una reservación

```http
  DELETE /hotel-app/reservations/${id}
```
![Screenshot](img/DELETE_one.png)
#### After delete when you search the reservation shows a message not found
![Screenshot](img/SEARCH_FOR_DELETED.png)

## **GRACIAS**