package uk.co.therhys.cmsapi.Db;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import uk.co.therhys.cmsapi.Article;

@Repository
public interface ArticleRepository extends CrudRepository<Article, Integer> {

}
