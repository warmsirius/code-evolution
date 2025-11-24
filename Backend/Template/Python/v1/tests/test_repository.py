from src import model, repository


def test_repository_can_save_batch(session):
    batch = model.Batch("batch1", "ADORABLE-SETTEE", 100, eta=None)
    repo = repository.SqlAlchemyRepository(session).add(batch)
    repo.add(batch)
    session.commit() # 将commit保留在repo外,并将其作为调用者的责任，这样有利有弊，第6章讲解

    rows = list(session.execute(
        'SELECT reference, sku, purchased_quantity, eta FROM "batches"'
    ))
    assert rows == [("batch1", "ADORABLE-SETTEE", 100, None)]