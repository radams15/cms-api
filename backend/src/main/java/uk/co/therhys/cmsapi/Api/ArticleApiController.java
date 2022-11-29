package uk.co.therhys.cmsapi.Api;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.lang.NonNull;
import org.springframework.web.bind.annotation.*;
import uk.co.therhys.cmsapi.Article;
import uk.co.therhys.cmsapi.Db.ArticleRepository;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

@RestController
public class ArticleApiController {
    @Autowired()
    private ArticleRepository articleRepository;

    @GetMapping("/api/v1/article/{id}")
    public ResponseEntity<Article> articleById(@PathVariable(value = "id") int id) {
        Article article = articleRepository.findById(id).orElse(null);

        if (article == null) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }

        return new ResponseEntity<>(article, HttpStatus.OK);
    }

    @PostMapping("/api/v1/article")
    public ResponseEntity<Integer> addArticle(@RequestBody @NonNull Article article) {
        Article savedArticle = articleRepository.save(article);

        return new ResponseEntity<>(savedArticle.getId(), HttpStatus.OK);
    }

    @GetMapping("/api/v1/article")
    public ResponseEntity<List<Article>> allArticles() {
        List<Article> articles = StreamSupport
            .stream(articleRepository.findAll().spliterator(), false)
            .collect(Collectors.toList());

        if (articles == null || articles.isEmpty()) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }

        return new ResponseEntity<>(articles, HttpStatus.OK);
    }

    @GetMapping("/api/v1/articleIds")
    public ResponseEntity<List<Integer>> allArticleIds() {
        List<Integer> articles = StreamSupport
            .stream(articleRepository.findAll().spliterator(), false)
            .map(
                Article::getId
            )
            .collect(Collectors.toList());

        if (articles == null || articles.isEmpty()) {
            return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        }

        return new ResponseEntity<>(articles, HttpStatus.OK);
    }
}
