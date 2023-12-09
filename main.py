from models.operation import Operation
from settings import OPERATIONS_PATH
from utils import get_all_operations, get_operations_instances, sort_operations_by_date


def main():
    all_operations: list[dict] = get_all_operations(OPERATIONS_PATH)
    operations_instances: list[Operation] = get_operations_instances(all_operations)
    sort_operations: list[Operation] = sort_operations_by_date(operations_instances)
    for operation in sort_operations[:5]:
        print(operation)
        print()


if __name__ == '__main__':
    main()
