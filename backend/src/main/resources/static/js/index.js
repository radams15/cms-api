const apiBase = "/api/v1";

function formatEpoch(epochTime){
    return new Date(epochTime + (new Date().getTimezoneOffset() * -1)).toISOString();
}

function loadArticle(article){
    $("#articleTitle").html(article.title);
    $("#articleSubTitle").html( article.subTitle);
    $("#articlePublishDate").html(formatEpoch(article.published));
    $("#articleImage").attr("src", article.headerImg);
    $("#articleContent").html(article.content);
}

function addArticleRow(article){
    let articleTable = $("#articleTable");

    let row = $("<tr>")

    var goLink = $('<button>');
    goLink.html(article.title);

    goLink.click(function () {
        loadArticle(article);
    })

    articleTable.append(row.append(goLink));
}

function loadArticleIds(){
    const req = new XMLHttpRequest();

    req.addEventListener("load", function(){
        var data = JSON.parse(this.responseText);

        data.forEach(addArticleRow)
    });

    req.open("GET", `${apiBase}/article/`);
    req.send();
}

loadArticleIds();