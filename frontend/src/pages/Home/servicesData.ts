import PetSitter from "../../assets/notes-lying-cat 1.svg";
import PetSupply from "../../assets/notes-dog 2.svg";
import PetVet from "../../assets/pet_vet.svg";
import IconBones from "../../assets/bones.svg";
import IconCheck from "../../assets/check.svg";

import {
  HowItWorksDataProps,
  InfoDataProps,
  ServiceDataProps,
} from "./interfaces/ServiceDataProps";

export const servicesData: ServiceDataProps[] = [
  {
    title: "Pet Sitter",
    description:
      "Suporte emergencial para tutores sem opções, nossos voluntários dedicados garantem cuidado e tranquilidade para seus pets.",
    linkText: "Ver mais",
    image: PetSitter,
    link: "#pet-sitter",
  },
  {
    title: "Pet Supply",
    description:
      "Estabelecemos parcerias com lojas para a doação de alimentos e utensílios para pets prestes a vencer, reduzindo o desperdício e ajudando animais necessitados.",
    linkText: "Ver mais",
    image: PetSupply,
    link: "#pet-supply",
  },
  {
    title: "Pet Free Vet",
    description:
      "Integrarmos nosso serviço com universidades veterinárias, onde estudantes oferecem atendimento prático para pets, ampliando nossa rede de apoio e cuidado.",
    linkText: "Ver mais",
    image: PetVet,
    link: "#pet-free-vet",
  },
];

export const infoData: InfoDataProps[] = [
  {
    icon: IconBones,
    title: "Conectando Tutores e Voluntários",
    description:
      "Estamos começando nossa jornada para conectar tutores preocupados com voluntários dedicados, proporcionando uma rede de apoio para o cuidado do seu animal de estimação.",
  },
  {
    icon: IconBones,
    title: "Rede de Apoio Essencial",
    description:
      "Somos uma rede 100% voluntária. Em situações de ansiedade, emergências repentinas ou simplesmente para promover a interação social dos pets, nossa plataforma oferece um apoio confiável.",
  },
  {
    icon: IconBones,
    title: "Comunidade de Cuidado Mútuo",
    description:
      "Promovemos uma comunidade de cuidado e apoio mútuo, onde tutores responsáveis e pessoas dispostas a ajudar podem se conectar e colaborar para o bem-estar dos animais de estimação.",
  },
];

export const howItWorksData: HowItWorksDataProps[] = [
  {
    icon: IconCheck,
    title: "Encontre um Pet Sitter",
    description: "Encontre o voluntário ideal para o seu pet em nosso site.",
  },
  {
    icon: IconCheck,
    title: "Agende um Horário",
    description:
      "           Entre em contato com o Pet Sitter pelo WhatsApp para combinar a data e hora em que precisa de apoio.",
  },
  {
    icon: IconCheck,
    title: "Agendamento Confirmado",
    description:
      "Depois de confirmar com o Pet Sitter, é só aguardar o dia e garantir que seu pet tenha um tempo maravilho.",
  },
  {
    icon: IconCheck,
    title: "Envie os Detalhes do Pet",
    description:
      "   Para garantir o melhor cuidado para o seu pet,             forneça ao Pet Sitter os seguintes dados ao entrar em contato (Nome, Raça, Idade, Gênero, Estado de saúde, Histórico médico (se houver), Medicações (se estiver tomando)).",
  },
];
