document.addEventListener('DOMContentLoaded', function() {
    var select = document.getElementById('id_tags');
    var chipList = document.getElementById('tags-chip-list');
    var showSelectBtn = document.getElementById('show-select-btn');
    var tagsSelectBlock = document.getElementById('tags-select-block');
    var hideSelectBtn = document.getElementById('hide-select-btn');
    var addForm = document.getElementById('add-tag-form');
    var saveBtn = document.getElementById('save-tag-btn');
    var cancelBtn = document.getElementById('cancel-tag-btn');
    var newTagTitle = document.getElementById('new-tag-title');
    var newTagDescr = document.getElementById('new-tag-descr');

    function updateChips() {
        chipList.innerHTML = '';
        Array.from(select.selectedOptions).forEach(function(option) {
            var chip = document.createElement('span');
            chip.className = 'chip';
            chip.textContent = option.text;
            chipList.appendChild(chip);
        });
    }
    if (select && chipList) {
        select.addEventListener('change', updateChips);
        updateChips();
    }

    if (showSelectBtn && tagsSelectBlock) {
        showSelectBtn.addEventListener('click', function() {
            tagsSelectBlock.style.display = 'flex';
            showSelectBtn.style.display = 'none';
        });
    }
    if (hideSelectBtn && tagsSelectBlock && showSelectBtn) {
        hideSelectBtn.addEventListener('click', function() {
            tagsSelectBlock.style.display = 'none';
            showSelectBtn.style.display = 'inline-block';
        });
    }
    if (saveBtn && newTagTitle && newTagDescr) {
        saveBtn.addEventListener('click', function() {
            // Здесь должен быть AJAX-запрос на сервер для создания нового тега
            // После успешного создания можно добавить тег в select
            alert('Добавление нового тега реализуется через сервер (AJAX)');
        });
    }
    if (addForm && tagsSelectBlock) {
        var addTagBtn = document.createElement('button');
        addTagBtn.textContent = '+';
        addTagBtn.className = 'add-tag-btn';
        addTagBtn.style.marginLeft = '4px';
        // Можно добавить логику для открытия addForm внутри select блока
    }
    if (cancelBtn && addForm) {
        cancelBtn.addEventListener('click', function() {
            addForm.style.display = 'none';
            newTagTitle.value = '';
            newTagDescr.value = '';
        });
    }
});
