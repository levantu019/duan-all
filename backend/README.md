# Note
- Run Docker
    ```
        docker-compose -f ./docker-compose.backend.yml up -d
    ```
- Tạo superuser:
    ```
        python manage.py createsuperuser
    ```
-   Đối với chạy thông thường:
        Copy 
        ```
            attach/custom_geo_field 
        ```
        dán vào 
        ```
            /venv/Lib/site-packages/django/contrib/gis/templates/gis/admin
        ```
-   Đối với chạy trong Docker:
        Vào hệ điều hành của Container django, copy /duan/attach/custom_geo_field dán vào /site-packages/django/contrib/gis/templates/gis/admin, ví dụ:
        ```
            cp -R /duan/attach/custom_geo_field /usr/local/lib/python3.6/site-packages/django/contrib/gis/templates/gis/admin
        ```
-   Lỗi khi makemigrations database:
    *   Trong file dulieuquantri/admin.py, dòng 158 giúp đổi app name của Group model (vì ban đầu Group nằm trong app auth của django, vì vậy thực hiện bước này để chuyển model sang app mới). Tuy nhiên xảy ra vấn đề là nếu thực hiện bước này đồng thời với quá trình tạo db thì sẽ dẫn đến một số bảng không thể tạo (auth_groups, auth_groups_permissions). Chính vì vậy, ở phiên bản này đang giải quyết vấn đề này bằng cách tạo db xong mới thực hiện đổi app cho Group.