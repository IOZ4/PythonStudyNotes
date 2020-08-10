##django基本理解
###基本原理###
**MTV 模型**

- M: model **模型**负责对数据的处理
- V: view **视图**负责处理用户请求，调用M和T，响应请求
- T: Template **模板**负责如何显示数据（产生html界面）
- **一个请求的一生**
- urls控制器-->view.py视图-->model.py模型-->数据库-->model.py-->view.py-->templates模板-->用户

- **创建项目** 在目标文件夹下执行(`django-admin startproject 项目名`)
- **创建应用** 在项目文件夹下执行(`python manage.py startapp 应用名`)
- **激活应用** setting.py 中在INSTALLED_APPS 列表中添加应用名 激活应用
- **配置数据库** 修改setting文件中的database
- **创建模型类** 在应用目录下的models.py文件中
- **生成迁移文件** 执行(`python manage.py makemigrations`)
- **执行迁移** 执行(`python manage.py migrate`)
- **配置模板路径** 在setting中的templates templates放置在manage同级目录(`'DIRS':[os.path.join(BASE_ DIR,’templates')],`)
- **配置urls控制器** 修改项目文件的urls.py和应用文件的urls.py来控制请求的流向 
- **创建视图** 返回html文件 显示数据