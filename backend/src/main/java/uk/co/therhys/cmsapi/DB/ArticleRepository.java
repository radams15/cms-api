package uk.co.therhys.cmsapi.DB;

import org.springframework.data.repository.CrudRepository;
import uk.co.therhys.cmsapi.Article;

public interface ArticleRepository extends CrudRepository<Article, Integer> {

}
