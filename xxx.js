ymaps.geocode('Москва').then(function (res) {
    var moscowCoords = res.geoObjects.get(0).geometry.getCoordinates();
    // Координаты Нью-Йорка
    ymaps.geocode('Нью-Йорк').then(function (res) {
        var newYorkCoords = res.geoObjects.get(0).geometry.getCoordinates();
        // Расстояние
        alert(ymaps.formatter.distance(
            ymaps.coordSystem.geo.getDistance(moscowCoords, newYorkCoords)
        ));
    });
});