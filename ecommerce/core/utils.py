"""Utils functions for core app."""


def get_user_media_path_prefix(instance, filename):
    return f"users/{instance.slug}/{filename}"
