
    const data_list = document.getElementById('data-list');
    const editButtons = document.querySelectorAll('.edit-button');

    editButtons.forEach(button => {
        button.addEventListener('click', () => {
            const key = button.dataset.key;
            const li = button.parentElement;
            const currentValue = li.querySelector('b').nextSibling.nodeValue;

            // Create an input field for editing
            const input = document.createElement('input');
            input.type = 'text';
            input.value = currentValue;

            // Replace the current value with the input field
            li.replaceChild(input, li.querySelector('b').nextSibling);

            // Create a save button
            const saveButton = document.
