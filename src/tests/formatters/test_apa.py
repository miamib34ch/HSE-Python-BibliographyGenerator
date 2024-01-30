"""
Тестирование функций оформления списка источников по APA
"""

from formatters.base import BaseCitationFormatter
from formatters.models import BookModel, InternetResourceModel, ArticlesCollectionModel, DissertationModel, JournalArticleModel
from formatters.styles.apa import APABook, APAInternetResource, APACollectionArticle, APADissertation, APAJournalArticle


class TestAPA:
    """
    Тестирование оформления списка источников согласно APA
    """

    def test_book(self, book_model_fixture: BookModel) -> None:
        """
        Тестирование форматирования книги.

        :param BookModel book_model_fixture: Фикстура модели книги
        :return:
        """

        model = APABook(book_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство (3-е изд. – ) СПб.: Просвещение, 999 с."
        )

    def test_internet_resource(
        self, internet_resource_model_fixture: InternetResourceModel
    ) -> None:
        """
        Тестирование форматирования интернет-ресурса.

        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :return:
        """

        model = APAInternetResource(internet_resource_model_fixture)

        assert (
            model.formatted
            == "Ведомости (01.01.2021) Наука как искусство https://www.vedomosti.ru"
        )

    def test_articles_collection(
        self, articles_collection_model_fixture: ArticlesCollectionModel
    ) -> None:
        """
        Тестирование форматирования сборника статей.

        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :return:
        """

        model = APACollectionArticle(articles_collection_model_fixture)

        assert (
            model.formatted
            == "Иванов И.М., Петров С.Н. (2020) Наука как искусство, Сборник научных трудов СПб.: АСТ, 25-30 с."
        )

    def test_dissertation(self, dissertation_fixture: DissertationModel) -> None:
        """
        Тестирование форматирования диссертации.

        :param DissertationModel dissertation_fixture: Фикстура модели диссертации
        :return:
        """

        model = APADissertation(dissertation_fixture)

        assert (
                model.formatted
                == "Иванов И.М. (2020) Наука как искусство, дис. [д-р. / канд. экон. 01.01.01] СПб., 199 с."
        )

    def test_journal_article(
            self, journal_article_fixture: JournalArticleModel
    ) -> None:
        """
        Тестирование форматирования статьи из журнала.

        :param JournalArticleModel journal_article_fixture: Фикстура модели статьи журнала
        :return:
        """

        model = APAJournalArticle(journal_article_fixture)

        assert (
                model.formatted
                == "Иванов И.М., Петров С.Н. (2020) Наука как искусство. Научный журнал, 1 25-30 с."
        )

    def test_citation_formatter(
        self,
        book_model_fixture: BookModel,
        internet_resource_model_fixture: InternetResourceModel,
        articles_collection_model_fixture: ArticlesCollectionModel,
        dissertation_fixture: DissertationModel,
        journal_article_fixture: JournalArticleModel,
    ) -> None:
        """
        Тестирование функции итогового форматирования списка источников.

        :param BookModel book_model_fixture: Фикстура модели книги
        :param InternetResourceModel internet_resource_model_fixture: Фикстура модели интернет-ресурса
        :param ArticlesCollectionModel articles_collection_model_fixture: Фикстура модели сборника статей
        :param DissertationModel dissertation_fixture: Фикстура модели диссертации
        :param JournalArticleModel journal_article_fixture: Фикстура модели статьи журнала
        :return:
        """

        models = [
            APABook(book_model_fixture),
            APAInternetResource(internet_resource_model_fixture),
            APACollectionArticle(articles_collection_model_fixture),
            APADissertation(dissertation_fixture),
            APAJournalArticle(journal_article_fixture),
        ]
        result = BaseCitationFormatter(models).format()

        # тестирование сортировки списка источников
        assert result[0] == models[1]
        assert result[1] == models[3]
        assert result[2] == models[0]
        assert result[3] == models[2]
        assert result[4] == models[4]
