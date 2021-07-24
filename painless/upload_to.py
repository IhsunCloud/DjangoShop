def product_directory_path(instance, filename):
    """ file will be uploaded to --> MEDIA_ROOT/product_<id>/<filename> """
    return 'product_{0}/{1}'.format(instance.id, filename)

def post_directory_path(instance, filename):
    """ file will be uploaded to --> MEDIA_ROOT/post_<id>/<filename> """
    return 'post_{0}/{1}'.format(instance.id, filename)