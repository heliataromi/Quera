def sort_dependencies(packages, package_name):
    package_dependencies = []

    def find_dependencies(dependencies):
        for dependency in dependencies:
            if dependency in package_dependencies:
                package_dependencies.remove(dependency)
            package_dependencies.insert(0, dependency)

            find_dependencies(packages[dependency])

    find_dependencies(packages[package_name])

    return package_dependencies
