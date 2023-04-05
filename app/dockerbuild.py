import argparse
import sys
import docker


def build_docker_image(dockerfile, image_name, image_tag):
    client = docker.from_env()

    try:
        client.images.get(f'{image_name.lower()}:{image_tag}')
        print(f'Imaginea Docker {image_name.lower()}:{image_tag} există deja!')
    except docker.errors.ImageNotFound:
        print(f'Creez imaginea Docker {image_name.lower()}:{image_tag}...')

        build_args = {'DOCKERFILE': dockerfile}
        client.images.build(path='.', tag=f'{image_name.lower()}:{image_tag}', buildargs=build_args)

        print(f'Imaginea Docker {image_name.lower()}:{image_tag} a fost creată cu succes!')


def deploy_docker_image(image_name, image_tag):
    client = docker.from_env()

    try:
        client.images.get(f'{image_name.lower()}:{image_tag}')
    except docker.errors.ImageNotFound:
        print(f'Imaginea Docker {image_name.lower()}:{image_tag} nu există! Creează imaginea folosind opțiunea "build" mai întâi.')
        sys.exit(1)

    container_name = f'{image_name.lower()}_{image_tag}'

    try:
        client.containers.get(container_name).remove(force=True)
        print(f'Containerul existent cu numele {container_name} a fost eliminat.')
    except docker.errors.NotFound:
        pass

    client.containers.run(f'{image_name.lower()}:{image_tag}', name=container_name, detach=True)
    print(f'Containerul a fost creat cu succes cu numele {container_name} și rulează acum.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script pentru construirea și implementarea imaginilor Docker.')
    parser.add_argument('action', choices=['build', 'deploy'], help='Acțiunea de realizat.')
    parser.add_argument('--dockerfile', default='Dockerfile', help='Calea către fișierul Dockerfile.')
    parser.add_argument('--image-name', required=True, help='Numele imaginii Docker.')
    parser.add_argument('--image-tag', default='latest', help='Eticheta imaginii Docker.')

    args = parser.parse_args()

    if args.action == 'build':
        build_docker_image(args.dockerfile, args.image_name, args.image_tag)
    elif args.action == 'deploy':
        deploy_docker_image(args.image_name, args.image_tag)
