<!DOCTYPE html>
<html>
<head>
    <%block name='head'>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>${APP_CODE}</title>
    <meta name="description" content=""/>
    <meta name="author" content=""/>
	<!-- bootstrap css -->
	<link href="${REMOTE_STATIC_URL}v3/assets/bootstrap-3.3.4/css/bootstrap.min.css" rel="stylesheet">
	<!-- 禁止bootstrap 响应式 （app根据自身需求启用或禁止bootstrap响应式） -->
	<link href="${REMOTE_STATIC_URL}v3/assets/bootstrap-3.3.4/css/bootstrap_noresponsive.css" rel="stylesheet">
    <!-- jquery ui css-->
    <link href="${REMOTE_STATIC_URL}v3/assets/jquery-ui-1.11.0.custom/jquery-ui.min.css" rel="stylesheet">
    <!-- 平台cs	 -->
	<link href="${REMOTE_STATIC_URL}v3/bk/css/bk.css" rel="stylesheet">
    <style>
    	/*如果你需要给你的应用固定高度和宽度，请在这里修改*/
		body {min-width:1202px;}
		.container{
			width:auto;
			min-width: 1200px;
			max-width:1400px;
		}
	</style>
	</%block>
</head>
<body>
    <!--顶部导航 Start-->
	<nav class="navbar navbar-default king-horizontal-nav2" role="navigation">
	    <div class="container" style="width: 100%;">
	        <div class="navbar-header col-md-4 col-sm-4 col-xs-4 logo">
	            <a class="navbar-brand" href="${SITE_URL}mako/" style="font-size:24px;padding-top: 15px;color: #438bca;">
	                蓝鲸开发框架(mako模板)
	            </a>
	        </div>
	        <div class="collapse navbar-collapse navbar-responsive-collapse col-md-8 col-sm-8 col-xs-8" id="king-example-navbar-collapse-2" style="float:right;">
	            <ul class="nav navbar-nav" style="float:right;">
					<%
						home = contact = ''
						relative_path = APP_PATH
						if relative_path == SITE_URL + "mako/":
							home = 'king-navbar-active'
						elif relative_path == SITE_URL + "mako/contact/":
							contact = 'king-navbar-active'
					%>
	                <li class="${home}"><a href="${SITE_URL}mako/"><span>首页</span></a></li>
	            </ul>
	        </div>
	    </div>
	</nav>
	<!--顶部导航 End-->

    <!-- 固定宽度居中 start -->
    <div class="container">
    	<div class="">
        	<%block name='content'></%block>
    	</div>
    </div>
    <!-- 固定宽度表单居中 end -->

</body>
<%block name="base_js">
<!-- jquery js  -->
<script src="${REMOTE_STATIC_URL}v3/assets/js/jquery-1.10.2.min.js"></script>
<script src="${REMOTE_STATIC_URL}jquery/jquery.json-2.3.min.js"></script>
<!-- 处理jquery兼容问题，jQuery Migrate（迁移）插件包含了1.6.4以来存在但1.9已不支持所有API -->
<script src="${REMOTE_STATIC_URL}v3/assets/js/jquery-migrate-1.2.1.min.js"></script>
<!-- bootstrap js  -->
<script src="${REMOTE_STATIC_URL}v3/assets/bootstrap-3.3.4/js/bootstrap.min.js"></script>
<!-- jquery ui js-->
<script src="${REMOTE_STATIC_URL}v3/assets/jquery-ui-1.11.0.custom/jquery-ui.min.js"></script>
<!-- 平台 js  -->
<script src="${REMOTE_STATIC_URL}v3/bk/js/bk.js"></script>

<!-- 这个是全局配置，如果需要在js中使用app_code和site_url,则这个javascript片段一定要保留 -->
<script type="text/javascript">
	var app_code = "${APP_CODE}";			// 在蓝鲸系统里面注册的"应用编码"
	var site_url = "${SITE_URL}";			// app的url前缀,在ajax调用的时候，应该加上该前缀
	var remote_static_url = "${REMOTE_STATIC_URL}";   //远程资源链接，403页面需要，不要删除
    var debug_mode = JSON.parse("${DEBUG}");
</script>
<!--统计js  勿删-->
<script src="${REMOTE_STATIC_URL}analysis.js?v=${ STATIC_VERSION }"></script>
<script src="${STATIC_URL}account/login.js?v=${ STATIC_VERSION }"></script>
<script src="${STATIC_URL}js/csrftoken.js?v=${ STATIC_VERSION }"></script>
<script src="${STATIC_URL}js/settings.js?v=${ STATIC_VERSION }"></script>
</%block>
<!--
    这里放置子页面中，不在block的内容，一般为js，注意子模版中的js如果使用到以上js库，必须放置在block外
    只对直接子页面起效，若子页面被继承，且继承子页面的页面有不在block中的内容，则子页面也需添加 $ {next.body()}
    $ {next.body()}的位置决定了子页面不在block的内容被渲染的位置
    也可使用$ {self.body()}，但$ {self.body()}只渲染最终页面不在block中的内容，中间继承页面不在block的内容不做渲染
 -->
${next.body()}
</html>
