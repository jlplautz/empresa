from core.models import ActiveModel, TimeStampedModel


class Employee(TimeStampedModel, ActiveModel):
    """Funcionario da empresa.
    O salario só aparece para qurm tem permissão view_salary.
    """
    class Role(models.TextChoices): 
        MANAGER = "MANAGER", "Gerente"
        SELLER = "SELLER", "Vendedor"

    name = models.CharField(max_length=50)
    email = models.EmailField('e-mail', unique=True)
    role = models.CharField('cargo',max_length=20,choices=Role.choices)
    salary = models.DecimalField('salário', max_digits=10, decimal_places=2)
    hired_on = models.DateField('admissão')

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        permissions = [
            ("view_salary", "Pode ver o salário"),
        ]

    def __str__(self):
        return self.name