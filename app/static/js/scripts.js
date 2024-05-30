var modal = document.getElementById("createClientModal");
var btn = document.getElementById("createClientBtn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.querySelector("#searchInput");
    const searchBtn = document.querySelector("#searchBtn");
    const tableRows = document.querySelectorAll("tr[id^='client_']");

    searchBtn.addEventListener("click", function() {
        const query = searchInput.value.toLowerCase().trim();

        tableRows.forEach(function(row) {
            const clientName = row.children[1].textContent.toLowerCase();
            const clientAddress = row.children[2].textContent.toLowerCase();
            const cityPostalCode = row.children[3].textContent.toLowerCase();
            const cityName = row.children[4].textContent.toLowerCase();
            const phoneNumber = row.children[5].textContent.toLowerCase();

            const match =
                clientName.includes(query) ||
                clientAddress.includes(query) ||
                cityPostalCode.includes(query) ||
                cityName.includes(query) ||
                phoneNumber.includes(query);

            if (match) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const deleteClientModal = document.getElementById("deleteClientModal");
    const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
    const cancelDeleteBtn = document.getElementById("cancelDeleteBtn");
    const deleteButtons = document.querySelectorAll(".delete");

    deleteButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            event.preventDefault();
            deleteClientModal.style.display = "block";
            const clientId = button.getAttribute("href").split("/").pop();
            confirmDeleteBtn.setAttribute("data-client-id", clientId);
        });
    });

    confirmDeleteBtn.addEventListener("click", function() {
        const clientId = confirmDeleteBtn.getAttribute("data-client-id");
        window.location.href = `/delete/${clientId}`;
    });

    cancelDeleteBtn.addEventListener("click", function() {
        deleteClientModal.style.display = "none";
    });

    const closeDeleteModal = document.querySelector("#deleteClientModal .close");
    closeDeleteModal.addEventListener("click", function() {
        deleteClientModal.style.display = "none";
    });
});

window.onload = function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        var phoneNumberInput = document.getElementById('phone_number');
        var postalCodeInput = document.getElementById('city_postal_code');

        if (postalCodeInput.value.length !== 5) {
            alert("Postal code must be exactly 5 digits long.");
            event.preventDefault();
            return;
        }
        if (phoneNumberInput.value.length !== 10) {
            alert("Phone number must be exactly 10 digits long.");
            event.preventDefault();
            return;
        }

        if (phoneNumberInput.value[0] != '0') {
            alert("Phone number must start with 0.");
            event.preventDefault();
            return;
        }
    });
}
