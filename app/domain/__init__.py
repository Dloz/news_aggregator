def get_site_name_from_package(crawler):
    return crawler.__module__.split('.')[-2]