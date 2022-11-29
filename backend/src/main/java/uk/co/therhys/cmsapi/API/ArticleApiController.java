package uk.co.therhys.cmsapi.API;

import org.springframework.beans.factory.annotation.Autowired;
import uk.co.therhys.cmsapi.DB.ArticleRepository;

public class ArticleApiController {
    @Autowired
    private ArticleRepository articleRepository;
}
