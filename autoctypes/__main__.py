from . import code_generator, reconstruct, context, extractor, ctypes_ext
import click


@click.command()
@click.option("--source", "-s", required=True, multiple=True)
@click.option("--output", "-o", required=True)
@click.option("--lib", "-l", multiple=True)
@click.option("--name", "-n", multiple=True)
@click.option("--type-hints/--no-type-hints", "-t/-T", is_flag=True, default=True)
@click.option("--comments/--no-comments", "-c/-C", is_flag=True, default=True)
@click.option("--includes/--no-includes", "-i/-I", is_flag=True, default=False)
@click.option("--fluff/--no-fluff", "-f/-F", is_flag=True, default=True)
@click.option("--wrappers/--no-wrappers", "-w/-W", is_flag=True, default=True)
def main(source, output, lib, name, type_hints, comments, includes, fluff, wrappers):
    ctx = context.Context(
        [],
        [context.Library(*l.split(":", 1)) for l in lib],
        comments,
        type_hints,
        fluff,
        name,
        wrappers,
    )
    head = code_generator.CompositorCodeGenerator(
        (
            code_generator.ImportCodeGenerator(ctx),
            code_generator.CtxSetupCodeGenerator(ctx),
            *(
                code_generator.CoPyCodeGenerator(ext, ctx)
                for ext in ctypes_ext.TYPE_EXTENSIONS
            ),
        ),
        ctx,
    )
    body = []
    for src in source:
        e = extractor.Extractor(src, ctx, not includes)
        body.extend(e.extract_code_generators())

    with open(output, "w") as f:
        f.write(reconstruct.stringify_code_generator(head))
        f.write(
            reconstruct.stringify_code_generator(
                code_generator.CompositorCodeGenerator(body, ctx)
            )
        )


if __name__ == "__main__":
    main()
