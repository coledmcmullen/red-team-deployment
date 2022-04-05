class TemplateHost(object):
    """Host from template file."""
    def __init__(self, file, hostname, description, os):
        self.file = file
        self.hostname = hostname
        self.description = description
        self.os = os

