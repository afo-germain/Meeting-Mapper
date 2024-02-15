// Variables
const API_BASE_URL = "http://127.0.0.1:8000";

var markers = [
    "http://leafletjs.com/examples/custom-icons/leaf-red.png",
    "http://leafletjs.com/examples/custom-icons/leaf-green.png",
    "http://leafletjs.com/examples/custom-icons/leaf-orange.png"
];


var utilisateurs = []

const toogleBtn = document.querySelector("#toogle")
toogleBtn.addEventListener('click', event => {
    event.preventDefault()
    loadUsers()
})

const processBtn = document.querySelector('#process')
processBtn.addEventListener('click', (event) => {
    processBtn.innerHTML = "Processing..."
    event.preventDefault()
    process()
})

// Créer une carte Leaflet avec un emplacement de départ et un niveau de zoom
var map = L.map('map').setView([0, 0], 15, {
    reset: true,
    animate: false
});

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

loadUsers();

// Fonction pour ajouter un utilisateur
const formAjoutUtilisateur = document.querySelector('#ajouter-utilisateur');
formAjoutUtilisateur.addEventListener('submit', (event) => {
    event.preventDefault();
    nouvelUtilisateur = {
        id: 1,
        nom: document.querySelector('#nom').value,
        prenom: document.querySelector('#prenom').value,
        latitude: parseFloat(document.querySelector('#latitude').value),
        longitude: parseFloat(document.querySelector('#longitude').value),
        adresse: document.querySelector('#adresse').value,
    }

    addUser()
});

function loadUsers() {
    // Chargement des utilisateurs
    fetch(API_BASE_URL + '/users')
        .then(response => response.json())
        .then(data => {
            utilisateurs = data;
            afficherUtilisateurs();
            afficherTousEmplacements(utilisateurs);
        });
}

function addUser() {
    fetch(API_BASE_URL + '/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(nouvelUtilisateur),
    })
        .then(response => response.json())
        .then(data => {
            // Rafraîchir la liste des utilisateurs
            loadUsers()
            formAjoutUtilisateur.reset()
            nouvelUtilisateur = {
                id: 0,
                nom: "",
                prenom: "",
                latitude: 0,
                longitude: 0,
                adresse: "",
            };
        });
}

// Fonction pour afficher la liste des utilisateurs
function afficherUtilisateurs() {
    const tbody = document.querySelector('#liste-utilisateurs tbody');
    tbody.innerHTML = "<tbody></tbody>"
    utilisateurs.forEach(utilisateur => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${utilisateur.nom}</td>
            <td>${utilisateur.prenom}</td>
            <td>${utilisateur.latitude}</td>
            <td>${utilisateur.longitude}</td>
            <td>${utilisateur.adresse}</td>
        `;
        tbody.appendChild(tr);
    });
}

// Fonction pour afficher tous les emplacements sur la carte
function afficherTousEmplacements(utilisateurs) {
    utilisateurs.forEach((utilisateur) => {      
        var marker = L.marker([utilisateur.latitude, utilisateur.longitude]).addTo(map).bindPopup(`${utilisateur.nom} ${utilisateur.prenom} <br><b>${utilisateur.adresse}</b>`).openPopup();

        marker.on('click', function () {
            this.openPopup();
        });
    });
}

function process() {
    fetch(API_BASE_URL + '/meeting')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            var marker = L.marker([data.lat, data.lon]).addTo(map).bindPopup(`Meeting place<br><b>${data.display_name}</b>`).openPopup();
            
            marker.setIcon(new L.Icon({
                iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
                shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34],
                shadowSize: [41, 41]
              }));

            map.setView([data.lat, data.lon], 9,  {
                "animate": true,
                "pan": {
                  "duration": 10
                }
              })
    
            marker.on('click', function () {
                this.openPopup();
            });

            processBtn.innerHTML = "Process Meeting"
        }).catch((err) => {
            processBtn.innerHTML = "Error, try Again !"
        });

}
/*
// Fonction pour afficher le point de rencontre
function afficherPointRencontre(pointRencontre) {
  L.marker(pointRencontre, {
    icon: L.icon({
      iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
      shadowUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-shadow.png',
    }),
  }).addTo(map);
}
*/