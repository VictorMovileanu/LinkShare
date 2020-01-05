$(document).ready(function () {
    $(".category-card").map(function () {
        const categoryCard = this;
        const bookmarkList = $(categoryCard).find(".category-card__list");
        const url = this.dataset.searchUrl;
        let q = this.dataset.query;  // todo: search for some query parameters concat function
        // todo: urlencode query
        let page = 1;
        $.get(url + "?page=" + page + "&q=" + q, function (data) {
            // todo: refactor. duplicated code
            $(bookmarkList).html(data);
            page += 1;
        });
        $(bookmarkList).scroll(function () {
            if (this.clientHeight + $(this).scrollTop() >= this.scrollHeight) {
                q = categoryCard.dataset.query;
                $.get(url + "?page=" + page + "&q=" + q, function (data) {
                    $(bookmarkList).append(data);
                    page += 1;
                });
            }
        });
    });

    $(".category-card__search-input").map(function () {
        const categoryCard = $(this).closest(".category-card");
        const bookmarkList = $(categoryCard).find(".category-card__list");
        const url = categoryCard.data("search-url");
        this.addEventListener("keyup", function () {
            $(categoryCard).attr("data-query", this.value);
            $.get(url + "?page=" + 1 + "&q=" + this.value, function (data) {
                // todo: refactor. duplicated code
                $(bookmarkList).html(data);
            });
        })
    })
});
