def config_diff_checker(old_config, new_config):
    old = dict(item.split("=") for item in old_config)
    new = dict(item.split("=") for item in new_config)
    diff = {"added": [], "deleted": [], "changed": {}}
    diff["added"] = list(new.keys() - old.keys())
    diff["deleted"] = list(old.keys() - new.keys())
    for key in old.keys() & new.keys():
        if old[key] != new[key]:
            diff["changed"][key] = (old[key], new[key])
    return diff

def main():
    config_old = ["env=prod", "debug=false"]
    config_new = ["env=prod", "debug=true", "replicas=3"]
    diff = config_diff_checker(config_old, config_new)
    print("Differences found:")
    for category, keys in diff.items():
        if keys:
            print(f"  {category.capitalize()}: {', '.join(keys)}")

if __name__ == "__main__":
    main()
