from inep_data.importers.school_data import SchoolDataImporter

if __name__ == "__main__":
    import os
    from optparse import OptionParser

    parser = OptionParser(usage="importer <filename>")
    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.error("Specify a file path")

    if not os.path.isfile(args[0]):
        parser.error("File not found")

    importer = SchoolDataImporter(args[0])
    importer.import_data()
