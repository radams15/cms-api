package uk.co.therhys.cmsapi;

import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@Data
public class Article {
    private int id;
    private String title;
    private String subTitle;
    private String content;
    private String headerImg;
}
