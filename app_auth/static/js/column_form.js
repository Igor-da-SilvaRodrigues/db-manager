if (document.body.classList.contains('column')) {
    const foreignKeyBool = document.getElementById('foreign_key_bool');
    const tableField = document.getElementById('fk_table_field');
    const columnField = document.getElementById('fk_column_field');
    const fkTableSelect = document.getElementById('fk_table_select');
    const fkColumnSelect = document.getElementById('fk_column_select');
    const typeSelect = document.getElementById('select_type');
    const maxLengthField = document.getElementById('max_length_field');
    const maxLengthInput = maxLengthField.childNodes[3];
    const enumList = document.getElementById('enum_list');
    const enumAddOptionButton = document.getElementById('add_enum_option_button');
    const removeParentNodeButton = document.getElementsByClassName('remove-node');
    const enumTypeOptionField = document.getElementById('enum_type_options_field');
    const pkBoolField = document.getElementById('');

    const foreignKeyPipeline = (foreign_key_bool) => {
        if (foreign_key_bool.options[foreign_key_bool.selectedIndex].value == 1) {
            tableField.classList.add('show');
            fillForeignKeyColumnsField();
            columnField.classList.add('show');
            return;
        }

        tableField.classList.remove('show');
        columnField.classList.remove('show');
        tableField.selectedIndex = null;
        columnField.selectedIndex = null;
    };

    const fillForeignKeyColumnsField = () => {
        let columns = fkTableSelect.options[fkTableSelect.selectedIndex].getAttribute('data-columns');
        fkColumnSelect.innerHTML = "";
        const selected = fkTableSelect.options[fkTableSelect.selectedIndex].getAttribute('data-selected')

        JSON.parse(columns).sort().forEach((column) => {
            const option = document.createElement('option');
            option.value = column;
            option.innerText = column;

            console.log(selected);
            if (option.value === selected) {
                option.selected = true;
            }

            fkColumnSelect.appendChild(option);
        });

        if (fkColumnSelect.firstChild) {
            fkColumnSelect.firstChild.setAttribute('selected', true);
        }
    };

    const checkMaxLengthNeedDisplay = () => {
        if (typeSelect.options[typeSelect.selectedIndex].classList.contains('require-length')) {
            maxLengthField.classList.add('show');

            return;
        }

        maxLengthField.classList.remove('show');
        maxLengthInput.value = null;
    };

    const checkEnumOptionListNeedDisplay = () => {
        if (typeSelect.options[typeSelect.selectedIndex].classList.contains('require-options')) {
            enumTypeOptionField.classList.add('show');

            return;
        }

        enumTypeOptionField.classList.remove('show');
    };

    const addOptionToList = (list) => {
        const node = list.childNodes[1].cloneNode(true);
        node.value = null;
        node.classList.remove('not-delete');
        const deleteButton = node.childNodes[3];

        deleteButton.addEventListener('click', () => {
            if (!deleteButton.parentElement.classList.contains('not-delete')) {
                deleteButton.parentElement.remove();
            }
        });

        list.appendChild(node)
    };

    foreignKeyPipeline(foreignKeyBool);
    checkMaxLengthNeedDisplay();
    checkEnumOptionListNeedDisplay();

    enumAddOptionButton.addEventListener('click', () => addOptionToList(enumList));
    typeSelect.addEventListener('change', () => {
        checkMaxLengthNeedDisplay();
        checkEnumOptionListNeedDisplay();
    });
    foreignKeyBool.addEventListener('change', () => foreignKeyPipeline(foreignKeyBool));
    fkTableSelect.addEventListener('change', () => fillForeignKeyColumnsField());

    Array.from(removeParentNodeButton).forEach((element) => {
        element.addEventListener('click', () => {
            if (!element.parentElement.classList.contains('not-delete')) {
                element.parentElement.remove();
            }
        });
    });

    const message = document.getElementsByClassName('message');

    // if (message[0]) {
    //     setTimeout(() => {
    //         message[0].style.display = 'none';
    //     }, 3000)
    // }
}

