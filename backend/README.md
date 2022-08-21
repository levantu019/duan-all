# Note
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
