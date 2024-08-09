navigator.geolocation.getCurrentPosition(successCallback, errorCallback);

function successCallback(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    // Enviar esses dados para o backend
}

function errorCallback(error) {
    console.error('Erro ao obter a localização:', error);
}
