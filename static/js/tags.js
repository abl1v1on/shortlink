document.addEventListener("DOMContentLoaded", function() {
    const tagElements = document.querySelectorAll('.choices');
    tagElements.forEach(el => {
        new Choices(el, {
            removeItemButton: true,
            placeholderValue: "Выберите теги",
            searchPlaceholderValue: "Поиск тегов",
            itemSelectText: 'Нажмите, чтобы выбрать',
            noResultsText: 'Нет доступных тегов'
        });
    });
});
