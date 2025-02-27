const CAMPOS_CONCIERTOS = "id, artistaId, salaId, fecha, precio_min, precio_max";
const CAMPOS_SALAS = "id, direccion, lat, long, municipio, relevancia";
const CAMPOS_GENEROS = "id, nombre";
const CAMPOS_ARTISTAS = "id, nombre, imagen_url, descripcion, generos, relevancia";
const CAMPOS_PREFERENCIAS = "id, usuario, generoId";
const CAMPOS_USUARIOS = "usuario, contrasena, nombre, apellido, email, fnac";

module.exports = { CAMPOS_ARTISTAS, CAMPOS_SALAS, CAMPOS_GENEROS, CAMPOS_CONCIERTOS, CAMPOS_PREFERENCIAS, CAMPOS_USUARIOS };
