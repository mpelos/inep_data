if __name__ == "__main__":
    import os
    from optparse import OptionParser
    from inep_data.importers.enem import EnemSchoolImporter

    parser = OptionParser(usage="importer [options] <filename>")
    parser.add_option("-w", "--workers", type="int", dest="workers",
            help="Set the number of worker processes to import the file")

    (options, args) = parser.parse_args()

    if len(args) == 0:
        parser.error("Specify a file path")

    if not os.path.isfile(args[0]):
        parser.error("File not found")

    importer = EnemSchoolImporter(args[0])
    importer.import_data(number_of_workers = options.workers or 2)
