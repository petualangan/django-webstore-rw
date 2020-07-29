# django-webstore

1. install django
    ```commandline
    $ pip install django
    ```
   
2. memulai project baru, syntax: `django-admin startpoject nama_project`, maka django akan membuat folder dan file baru
    ```commandline
    $ django-admin startproject ecommerce
    ```
   
3. membuat aplikasi, yang nantinya bakal dikerjakan, syantax:
    ```commandline
    $ cd ecommerce 
    ecommerce$ python manage.py startapp store
    ```

4. edit file settings.py di folder ecommerce(anak), dibagian `INSTALLED_APPS ` tambahkan
    ```commandline
    'store.apps.StoreConfig',
    ```

5. mengetes apakah django sudah berjalan apa belum
    ```commandline
    $ python manage.py runserver
    ```