document.addEventListener('DOMContentLoaded', function () {
    function toggleField(checkboxId, fieldId, inputId) {
        const checkbox = document.getElementById(checkboxId);
        const field = document.getElementById(fieldId);
        const input = document.getElementById(inputId);

        function updateField() {
            if (checkbox.checked) {
                field.style.display = 'block';
            } else {
                field.style.display = 'none';
                input.value = '';  // Очищення поля
            }
        }

        if (checkbox) {
            updateField();
            checkbox.addEventListener('change', updateField);
        }
    }

    toggleField('id_has_pet', 'pet_type_field', 'id_pet_type');
    toggleField('id_has_car', 'car_model_field', 'id_car_model');
});
