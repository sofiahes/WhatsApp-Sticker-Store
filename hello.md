## Rutas para el Flask (TODO)

1. Para la tabla `PERSONA`, `USUARIO` o `CREADOR` [Sign In / Login]
    + **POST** para el sign in (crear un nuevo usuario)
    + **GET** para el login (acceder a tu cuenta)
    + **PUT<id>** para actualizar los datos de tu cuenta
    + **DELETE<id>** para eliminar tu cuenta
2. Para la tabla `CARRITO`:
    + **GET<id>** para identificar el carrito de un usuario activo

3. Para la tabla `CARRITO` / `PERTENECE`:
    + **GET** para descar@gar todos los stickers del carrito
    + **POST** para añadir un sticker al carrito
    + **DELETE** para eliminar un sticker del carrito
4. Para la tabla `STICKER`: (melanie)
    + **GET** para que los stickers se muestren en el main (fetch)
    + **POST** para crear un nuevo sticker
    + **DELETE** para eliminar todos los stickers de un solo creador al borrar la cuenta
    + **GET<id>** para mostrar los stickers de un solo creador
    + **PUT<id>** para actualizar un sticker de un solo creador
    + **DELETE<id>** para eliminar un sticker
5. Para la tabla `COMENTARIO`: (melanie)
    + **GET<sticker_id>** para mostrar los comentarios de un sticker
    + **POST<sticker_id>** para crear un nuevo comentario para un sticker
    + **DELETE<sticker_id>** para eliminar todos los comentarios de un sticker
    + **PUT<id>** para editar un comentario
    + **DELETE<id>** para eliminar un comentario

