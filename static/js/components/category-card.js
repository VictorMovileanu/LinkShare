$(document).ready(function () {
    $(".category-card").map(function () {
        const categoryCard = this;
        const bookmarkList = $(categoryCard).find(".category-card__list");
        const url = this.dataset.searchUrl;
        let page = 1;
        $.get(url + "?page=" + page, function (data) {
            // todo: refactor. duplicated code
            $(bookmarkList).html(data);
            page += 1;
        });
        $(bookmarkList).scroll(function () {
            if (this.clientHeight + $(this).scrollTop() >= this.scrollHeight) {
                $.get(url + "?page=" + page, function (data) {
                    $(bookmarkList).append(data);
                    page += 1;
                });
            }
        });
    });
});
