document.addEventListener('DOMContentLoaded', (event) => {
    let selects = document.querySelectorAll('select');

    // Stocker les valeurs initiales
    let initialValues = Array.from(selects).map(select => select.options[select.selectedIndex].value);

    selects.forEach((select) => {
        let selectedOption = select.options[select.selectedIndex].value;
        selects.forEach((s) => {
            if (s !== select) {
                for (let option of s.options) {
                    if (option.value === selectedOption) {
                        option.disabled = true;
                    }
                }
            }
        });
    });

    selects.forEach((select, index) => {
        select.addEventListener('change', (event) => {
            // Réactivez toutes les options dans tous les champs de sélection
            selects.forEach((s) => {
                for (let option of s.options) {
                    // Si l'option est une valeur initiale et qu'elle est toujours sélectionnée par un autre champ de sélection, ne la réactivez pas
                    if (initialValues.includes(option.value) && Array.from(selects).some(select => select.options[select.selectedIndex].value === option.value)) {
                        continue;
                    }
                    option.disabled = false;
                }
            });

            // Désactivez l'option sélectionnée dans les autres champs de sélection
            selects.forEach((s) => {
                if (s !== event.target) {
                    for (let option of s.options) {
                        if (option.value === event.target.value) {
                            option.disabled = true;
                        }
                    }
                }
            });

            // Mettez à jour la valeur précédemment sélectionnée
            event.target.oldValue = event.target.value;
        });
    });
});