<!DOCTYPE html>
<html>
  <head>
    <!-- meta -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0">
<link rel="stylesheet" type="text/css" href="/css/common.css">

<link rel="shortcut icon" href="/images/site-logo.png">

<script type="text/javascript" src="/js/jquery-1.9.0.min.js"></script>
<script type="text/javascript" src="/js/google-code-prettify/prettify.js"></script>
<link  type="text/css" rel="stylesheet" href="/js/google-code-prettify/prettify.css"/>
<script>
  $(function(){
    // google code prettifyの有効化
    $("pre").addClass("prettyprint");
    function init(event){
      prettyPrint();
    }
    if(window.addEventListener)window.addEventListener("load",init,false);
    else if(window.attachEvent)window.attachEvent("onload",init);
    
    $(".to-top").click(function() {
      // ページの一番上までスクロールさせます。
      $('body, html').animate({scrollTop: 0}, 300, 'linear');;
    });
  });
</script>

<title>Title - Webシステム開発入門 - Perl/MojoliciousでWebシステム開発</title>
<meta name="description" content="#!/usr/bin/env perl">
  </head>
  <body>
    <div class="container">
      <div class="header">
        <!-- header -->
<h1>
  <a href="/">Webシステム開発入門 - Perl/MojoliciousでWebシステム開発</a>
</h1>

      </div>
      <div class="main">
        <div class="content">
          <div class="entry">
  <div class="top">
    <!-- top -->

  </div>
  <div class="middle">
    <p>
  #!/usr/bin/env perl
</p>
<p>
  use strict;
</p>
<p>
  use warnings;
</p>
<p>
  use utf8;
</p>
<p>
  use Encode 'encode';
</p>
<p>
  # Title mail form
</p>
<p>
  my $title = 'Mail form';
</p>
<p>
  # Content mail form
</p>
<p>
  my $content = <<"EOS";
</p>
<h2><a href="/test.cgi">Title</a></h2>
<div>
  Content
</div>
<p>
  EOS
</p>
<p>
  $content = build_html($title, $content);
</p>
<p>
  my $html = <<"EOS";
</p>
<p>
  Content-type: text/html; charset=UTF-8
</p>
<p>
  $content
</p>
<p>
  EOS
</p>
<p>
  print encode('UTF-8', $html);
</p>
<p>
  sub build_html {
</p>
  my ($title, $content) = @_;
  
  local $/;
  my $html = <DATA>;
  
  $html =~ s/\$TITLE/$title/;
  $html =~ s/\$CONTENT/$content/;
  
  return $html;
<p>
  }
</p>
<p>
  __DATA__
</p>

  </div>
  <div class="bottom">
    <!-- bottom -->

<div class="perlzemi-forum">
  <a rel="nofollow" href="https://docs.google.com/forms/d/e/1FAIpQLSe6ypMTx5XTh2KbsIgqgPMXNrC5Bo9FKRPVHM_o0jvrH_k28A/viewform">
    Perlゼミフォーラム - 環境構築・Perlプログラムの読み書きに困ったらここで質問(無料・5分で登録)
  </a>
</div>

  </div>
</div>

        </div>
        <div class="side">
          <!-- side -->
<div class="side-list">
  <div class="side-list-title">
    目次
  </div>
  <ul>
    <li><a href="/list.html">新着情報</a></li>
  </ul>
</div>

        </div>
      </div>
      <div class="footer">
        <!-- footer -->
<a href="https://kimoto-system.co.jp/message">サイト運営 木本システム <br>Copyright © Yuki Kimoto</a>

      </div>
    </div>
  </body>
</html>
