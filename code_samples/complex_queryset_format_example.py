# First option.
complex_queryset_format_example = SimpleModel.objects.filter(
    Q(is_active=True)
    | Q(is_in_list=False),
).filter(
    scraping_jobs__isnull=True,
).exclude(
    is_black_listed=True,
).annotate(
    not_disclosed_count=Count(
        'scraping_attempts',
        filter=Q(id_provider=id_provider),
    ),
).order_by(
    'not_disclosed_count',
)
# Second option.
complex_queryset_format_example = (
    SimpleModel.objects
    .filter(
        Q(is_active=True)
        | Q(is_in_list=False),
    )
    .filter(scraping_jobs__isnull=True)
    .exclude(is_black_listed=True)
    .annotate(
        not_disclosed_count=Count(
            'scraping_attempts',
            filter=Q(id_provider=id_provider),
        ),
    )
    .order_by('not_disclosed_count')
)
