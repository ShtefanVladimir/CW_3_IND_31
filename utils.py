import json

from models.operation import Operation


def get_all_operations(path) -> list[dict]:
    """
    Функция получения операций из файла
    :param path: путь к файлу
    :return: json с операциями
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_operations_instances(operations: list[dict]) -> list[Operation]:
    operations_instances = []
    for operation in operations:
        if operation and operation["state"] == "EXECUTED":
            operation_instance = Operation(
                pk=operation["id"],
                date=operation["date"],
                state=operation["state"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to=operation["to"],
            )
            operations_instances.append(operation_instance)
    return operations_instances


def sort_operations_by_date(operations: list[Operation]) -> list[Operation]:
    return sorted(operations, key=lambda operation: operation.date, reverse=True)
